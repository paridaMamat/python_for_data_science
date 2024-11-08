import shutil


def ft_tqdm(lst):
    """
    function that copy the function tqdm which for generation of progress bars
    """
    total = len(lst)
    columns = shutil.get_terminal_size().columns  # Get terminal width
    for i, item in enumerate(lst):
        percent = (i + 1) / total * 100
        bar_length = columns - 40  # Adjust based on terminal width
        bar = '█' * int(percent / 100 * bar_length)
        print(f'\r{int(percent)}%|{bar:<{bar_length}}|{i + 1}/{total}', end='')
        yield item

    print()
