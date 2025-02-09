
            args = args[2:]
            
    model = os.path.join(mode,"lda" + k,"final")
    words = os.path.join(mode,"vocab.dat")
    docs = os.path.join(mode,"docs.dat")

    pdf_file = args[0]
    (base,_) = os.path.splitext(pdf_file)
    
    text = os.popen("/usr/bin/pdftotext \"%s\" -" % pdf_file).read() # XXX safe filenames!

    vocab = words_to_dict(open(words).read().split())
    
    bow = make_bow(map(stem,tokens(text)),vocab)

    dat_file = base + ".dat"
    out = open(dat_file,"w")
    out.write(str(len(bow)))
    out.write(' ')