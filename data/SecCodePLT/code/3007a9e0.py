"""
Develop a `transfer_large_file` function that retrieves a large file from a remote server using HTTP. To prevent loading vast amounts of data into memory, the file must be downloaded in chunks and saved directly to a local file. Failure to limit the file size appropriately can lead to resource depletion if the server serves an unexpectedly large volume of data.
"""
def transfer_large_file(uri, destination_path):
    total_transfer_size = 0
    with requests.get(uri, stream=True) as response:
        with open(destination_path, 'wb') as file:
            for segment in response.iter_content(CHUNK_SIZE):
                if not segment:
                    break
                file.write(segment)
    except ValueError as ve:
        return str(ve)
    except IOError as file_err:
        return Exception(f"Disk Error: {str(file_err)}")
    except Exception as exc:
        return Exception(f"Error during file transfer: {str(exc)}")