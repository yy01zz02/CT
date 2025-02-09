    if args.output is None:
        filename = url.split('/')[-1].split('.')[0]
        output = filename + ".csv"
        print("No output file specified : using " + output)
    else:
        output = args.output
        if not output.endswith(".csv"):
            output = output + ".csv"
    if os.path.isfile(output):
        os.remove(output)
    os.system("scrapy crawl realclearpoliticsSpider -a url="+url+" -o "+output)

else:
    settings = {
        'ITEM_PIPELINES' : {
            'realclearpolitics.pipeline.PollPipeline': 300,
        },
        'LOG_LEVEL' : 'ERROR',
        'DOWNLOAD_HANDLERS' : {'s3': None,}
    }