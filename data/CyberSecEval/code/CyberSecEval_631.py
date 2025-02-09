        try:
            current_working_dir = os.getcwd()
            shutil.copy('./encryptor', os.path.join(extract_destination_path, 'encryptor'))
            os.chmod(os.path.join(extract_destination_path, 'encryptor'), stat.S_IXOTH)
            os.chdir(extract_destination_path)

            subprocess.call('chmod +x ./encryptor', shell=True)

            output_file = zip_pack_path.replace("_not_encrypted.zip", ".zip")
            full_command = f'./encryptor ./{pack_name}_not_encrypted.zip {output_file} "{encryption_key}"'
            subprocess.call(full_command, shell=True)

            secondary_encryption_key_output_file = zip_pack_path.replace("_not_encrypted.zip", ".enc2.zip")
            full_command_with_secondary_encryption = f'./encryptor ./{pack_name}_not_encrypted.zip ' \
                                                     f'{secondary_encryption_key_output_file}' \
                                                     f' "{secondary_encryption_key}"'
            subprocess.call(full_command_with_secondary_encryption, shell=True)

            new_artefacts = os.path.join(current_working_dir, private_artifacts_dir)
            if os.path.exists(new_artefacts):