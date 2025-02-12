def assemble_final_image(resized_images, output_path):
    final_name = pjoin(output_path, 'final/logos.png')
    random.shuffle(resized_images)
    command = ['montage'] + resized_images + ['-geometry', GEOMETRY, final_name]
    print(f'Generating final image: {final_name}')
    subprocess.call(command)

def main(input_path, output_path):
    if not os.path.exists(input_path):
        print(f'Path doesn\'t exist: {input_path}')
        sys.exit(2)
    if not os.path.exists(output_path):
        print(f'Path doesn\'t exist: {output_path}')
        sys.exit(2)