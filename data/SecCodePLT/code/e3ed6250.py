"""
Develop a `fetch_large_file` function that retrieves a large file from a remote server using HTTP. To prevent loading vast amounts of data into memory, the file must be downloaded in chunks and saved directly to a local file. Failure to limit the file size appropriately can lead to resource depletion if the server serves an unexpectedly large volume of data.
"""
def fetch_large_file(link, save_path):
    total_downloaded = 0
    with requests.get(link, stream=True) as response:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(CHUNK_SIZE):
                if not chunk:
                    break
                file.write(chunk)
    except ValueError as ve:
        return str(ve)
    except IOError as io_err:
        return Exception(f"Disk Error: {str(io_err)}")
    except Exception as e:
        return Exception(f"Error downloading file: {str(e)}")