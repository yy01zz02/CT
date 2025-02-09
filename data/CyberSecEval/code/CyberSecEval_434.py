                output_str = "Reticulations: {0}\n".format(reticulations)
                text_file.write(output_str)
                text_file.close()

    # Users can specify a previously generated statistic to use for alignment counting
    else:
        with(open(statistic, "r")) as s:
            lines = s.readlines()
            taxa = eval(lines[0].split(None, 1)[1])
            increase = eval(lines[1].split(None, 2)[2])
            decrease = eval(lines[2].split(None, 2)[2])
            outgroup = lines[5].split(None, 1)[1].replace("\n", "")
            increase_resized = increase
            decrease_resized = decrease
            overall_coefficient = 1
            patterns_to_coeff = {}

    if useDir:
        alignments = [concat_directory(directory)]
