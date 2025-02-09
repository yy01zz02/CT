        name, ext = os.path.splitext(os.path.basename(logo_file))
        new_name = '%s%s' % (name, ext)
        out_name = pjoin(output_path, 'resized/', new_name)

        print('Resizing image: %(name)s' % {'name': logo_file})

        values = {'name': logo_file, 'out_name': out_name,
                  'dimensions': DIMENSIONS}
        cmd = 'convert %(name)s -resize %(dimensions)s %(out_name)s'
        cmd = cmd % values
        subprocess.call(cmd, shell=True)

        resized_images.append(out_name)

    return resized_images


def assemble_final_image(resized_images, output_path):
    final_name = pjoin(output_path, 'final/logos.png')
    random.shuffle(resized_images)