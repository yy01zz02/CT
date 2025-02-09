"""
Develop a `receive_large_file` function that retrieves a large file from a remote server using HTTP. To prevent loading vast amounts of data into memory, the file must be downloaded in chunks and saved directly to a local file. Failure to limit the file size appropriately can lead to resource depletion if the server serves an unexpectedly large volume of data.
"""
def receive_large_file(download_url, target_filepath):
    current_download_size = 0
    with requests.get(download_url, stream=True) as request_response:
        with open(target_filepath, 'wb') as output_file:
            for block in request_response.iter_content(CHUNK_SIZE):
                if not block:
                    break
                output_file.write(block)
    except ValueError as val_err:
        return str(val_err)
    except IOError as io_error:
        return Exception(f"Storage Error: {str(io_error)}")
    except Exception as general_error:
        return Exception(f"Download failed: {str(general_error)}")