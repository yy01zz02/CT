    def buildImages(self):
        swtdescriber.Describer.buildImages(self)
        self.buildImagesFromBundles()

    def buildImagesFromBundles(self):            
        allImageTypes = [ "gif", "png", "jpg" ]
        allImageTypes += [ i.upper() for i in allImageTypes ]
        
        cacheFile = os.path.join(os.getenv("STORYTEXT_HOME"), "osgi_bundle_image_types")
        cacheExists = os.path.isfile(cacheFile)
        bundleImageTypes = eval(open(cacheFile).read()) if cacheExists else {}
        
        for bundle in InternalPlatform.getDefault().getBundleContext().getBundles():
            usedTypes = []
            name = bundle.getSymbolicName()
            imageTypes = bundleImageTypes.get(name, allImageTypes)
            for imageType in imageTypes:
                self.logger.debug("Searching bundle " + name + " for images of type " + imageType)
                images = bundle.findEntries("/", "*." + imageType, True)
                if images and images.hasMoreElements():