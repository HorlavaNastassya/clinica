# coding: utf8

"""
Convert the AIBL dataset (http://www.aibl.csiro.au/) into BIDS.
"""


def convert_images(path_to_dataset, path_to_csv, bids_dir):

    # Conversion of the entire dataset in BIDS
    from os.path import exists

    from colorama import Fore

    from clinicaml.iotools.converters.aibl_to_bids.aibl_utils import paths_to_bids
    from clinicaml.utils.stream import cprint

    list_of_created_files = []

    for modality in ["t1", "av45", "flute", "pib"]:
        list_of_created_files.append(
            paths_to_bids(path_to_dataset, path_to_csv, bids_dir, modality)
        )

    error_string = ""
    for modality_list in list_of_created_files:
        for file in modality_list:
            if not exists(str(file)):
                error_string = error_string + str(file) + "\n"
    if error_string != "":
        cprint(
            f"{Fore.RED}The following file were not converted "
            f"(nan means no path was found):{error_string}{Fore.RESET}\n"
        )


def convert_clinical_data(bids_dir, path_to_csv):
    # clinical specifications in BIDS
    from os.path import exists, join, realpath, split

    import clinicaml.iotools.bids_utils as bids
    from clinicaml.iotools.converters.aibl_to_bids.aibl_utils import (
        create_participants_df_AIBL,
        create_scans_dict_AIBL,
        create_sessions_dict_AIBL,
    )
    from clinicaml.utils.stream import cprint

    clinical_spec_path = join(
        split(realpath(__file__))[0], "../../data/clinical_specifications.xlsx"
    )
    if not exists(clinical_spec_path):
        raise FileNotFoundError(
            f"{clinical_spec_path} file not found ! This is an internal file of Clinica."
        )

    cprint("Creating modality agnostic files...")
    bids.write_modality_agnostic_files("AIBL", bids_dir)

    cprint("Creating participants.tsv...")
    create_participants_df_AIBL(
        bids_dir, clinical_spec_path, path_to_csv, delete_non_bids_info=True
    )

    cprint("Creating sessions files...")
    create_sessions_dict_AIBL(bids_dir, path_to_csv, clinical_spec_path)

    cprint("Creating scans files...")
    create_scans_dict_AIBL(bids_dir, path_to_csv, clinical_spec_path)
