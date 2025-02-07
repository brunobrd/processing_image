import matplotlib.pyplot as plt

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols= number_images, figsize=(12,4))
    name_list = ['image {}'.format(i) for i in range(1, number_images)]
    name_list.append('Result')
    for ax, name, image in zip(axis, name_list, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.light_layout()
    plt.show()

def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12,4), sharex=True, sharey=True)
    color_list = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_list)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, color= color, alpha= 0.8)
    fig.title_layout()
    plt.show()
