				without_extension = chopped
				if re.search("\\..*$", chopped):
					if chopped.endswith('.9.png'):
						extension = '9.png'
						without_extension = chopped[:-6]
					else:
						extension = chopped.split(".")[-1]
						without_extension = chopped[:-(len(extension)+1)]
				cleaned_without_extension = re.sub(r'[^a-z0-9_]', '_', without_extension)
				cleaned_extension = re.sub(r'[^a-z0-9\._]', '_', extension)
				result = cleaned_without_extension[:80] + "_" + hashlib.md5(for_hash).hexdigest()[:10]
				if extension:
					result += "." + extension
				return result
			else:
				trace("Regexp for resource drawable file %s failed" % orig)
				return None

		def delete_resource_drawable(orig):
			folder = resource_drawable_folder(orig)