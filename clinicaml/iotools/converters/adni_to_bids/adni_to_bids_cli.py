# coding: utf-8

import clinicaml.engine as ce

def str2bool(v):
    import argparse
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


class AdniToBidsCLI(ce.CmdParser):
    def define_name(self):
        """Define the sub-command name to run this command."""
        self._name = "adni-to-bids"

    def define_description(self):
        """Define a description of this command."""
        self._description = "Convert ADNI (http://adni.loni.usc.edu/) into BIDS"

    def define_options(self):
        """Define the sub-command arguments."""
        self._args.add_argument(
            "dataset_directory", help="Path to the ADNI images directory."
        )
        self._args.add_argument(
            "clinical_data_directory", help="Path to the ADNI clinical data directory."
        )
        self._args.add_argument("bids_directory", help="Path to the BIDS directory.")
        self._args.add_argument(
            "-c",
            "--clinical_data_only",
            action="store_true",
            help="(Optional) Given the path to an already existing ADNI BIDS folder, convert only "
            "the clinical data. Mutually exclusive with --force_new_extraction",
        )
        self._args.add_argument(
            "-f",
            "--force_new_extraction",
            action="store_true",
            help="(Optional) Forces the extraction of data even if the image already exists in the "
            "bids_directory. Mutually exclusive with --clinical_data_only",
        )
        self._args.add_argument(
            "-sl",
            "--subjects_list",
            help="(Optional) A path to a .txt file containing a list of subject to convert "
            "(one for each row).",
        )
        self._args.add_argument(
            "-m",
            "--modalities",
            nargs="+",
            default=["T1", "PET_FDG", "PET_AMYLOID", "PET_TAU", "DWI", "FLAIR", "fMRI"],
            choices=["T1", "PET_FDG", "PET_AMYLOID", "PET_TAU", "DWI", "FLAIR", "fMRI"],
            help="(Optional) Convert only the list of selected modalities. "
            "By default all modalities are converted. Modalities available: "
            "T1, PET_FDG, PET_AMYLOID, PET_TAU, DWI, FLAIR, fMRI.",
        )

        self._args.add_argument(
            "-oe",
            "--only_existing_data", type=str2bool, default=False,
            help="(Optional) if set to True, only files in provided source folder will be considered",
        )

    def run_command(self, args):
        from clinicaml.iotools.converters.adni_to_bids.adni_to_bids import AdniToBids
        from clinicaml.utils.exceptions import ClinicaParserError
        from colorama import Fore

        adni_to_bids = AdniToBids()

        # Check dcm2nii and dcm2niix dependencies
        adni_to_bids.check_adni_dependencies()

        if args.clinical_data_only and args.force_new_extraction:
            raise ClinicaParserError(
                f"{Fore.RED}\n[Error] Arguments clinical_data_only and force_new_extraction are mutually exclusive.{Fore.RESET}"
            )

        if not args.clinical_data_only:
            adni_to_bids.convert_images(
                self.absolute_path(args.dataset_directory),
                self.absolute_path(args.clinical_data_directory),
                self.absolute_path(args.bids_directory),
                args.subjects_list,
                args.only_existing_data,
                args.modalities,
                args.force_new_extraction,
            )

        adni_to_bids.convert_clinical_data(
            self.absolute_path(args.clinical_data_directory),
            self.absolute_path(args.bids_directory),
        )
