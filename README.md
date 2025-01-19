# Numpy.org

## Getting Started

To contribute to the website, you'll first need to install the *extended
version* of Hugo.

### 1. Install Hugo (Extended Version)

The website is powered by **Hugo**, a fast and flexible static site generator. To ensure you have access to all the necessary features for contributing to the project, you must install the **extended version of Hugo**. The extended version includes additional capabilities, such as enhanced image processing, which are critical for content optimization and functionality.

### Step-by-Step Installation:

- Visit the official [Hugo installation page](https://gohugo.io/getting-started/installing/) for detailed instructions on installing Hugo for various platforms.
- **Important**: Ensure that you specifically download the **extended version** of Hugo. The standard version does not include all the features required for this project, and using it may result in errors when running the deployment server or starting the application.

Once Hugo is installed, you can confirm that everything is set up correctly by checking the version:

```bash
hugo version
```

This command should return the installed version of Hugo, and it should reflect the extended version.

### 2. Clone the Repository and Install the Theme

With Hugo successfully installed, the next step is to set up the project repository and its theme.

- **Clone the repository** using Git:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

- **Install the theme** for the website by initializing the Git submodules:

    ```bash
    git submodule update --init --recursive
    ```


This will download and configure all the theme files necessary to render the website as intended.

### 3. Install `make` on Ubuntu

In order to run the `make serve` command and start the development server, you need to install `make` on your system. `make` is a tool used to automate and streamline processes, such as compiling code or serving the site.

### Steps to Install `make` on Ubuntu:

1. **Open your terminal**.
2. **Update the package list** to ensure your system is aware of the latest available versions:

    ```bash
    sudo apt update
    ```

3. **Install the `make` utility**:

    ```bash
    sudo apt install make
    ```

4. **Verify the installation** by checking the installed version of `make`:

    ```bash
    make --version
    ```


If `make` has been successfully installed, you should see the version information displayed in the terminal.

### 4. Starting the Development Server

Once you have completed the setup and installed all necessary dependencies, you're ready to start the local development server. On Ubuntu, you can do this using the `make serve` command, which is part of the project's Makefile.

Simply run the following command:

```bash
make serve
```

This will build and serve the website locally, allowing you to preview your changes. The site should now be accessible at: [**`*http://localhost:1313*`**](http://localhost:1313/)

### Alternative for Windows Users

If you're using a platform like Windows and `make` is not available, you can run the following commands instead:

```bash
python gen_config.py
hugo server
```

Make sure you have the **extended version of Hugo installed** before running these commands.

- **Error Handling**: If you encounter any errors while running `make serve`, it is likely related to missing dependencies or an incorrect installation. Double-check that Hugo's extended version is installed and that all steps were followed.
- **Ensure Proper Theme Setup**: Missing theme files can also cause issues. Make sure to initialize the submodules correctly using `git submodule update --init --recursive`.


## User Experience (UX)

### NumPy Color Palette

![#013243 Warm Black](./static/images/content_images/swatch_013243_warm_black.png) `RGB 1/50/67 | HEX #013243 | NumPy Warm Black`

![#4D77CF Han Blue](./static/images/content_images/swatch_4D77CF_han_blue.png) `RGB 77/119/207 | HEX #4D77CF | NumPy Deep Blue`

![#4DABCF Maximum Blue](./static/images/content_images/swatch_4DABCF_maximum_blue.png) `RGB 77/171/207 | HEX #4DABCF | NumPy Ndarray Blue`

![#6C7A89 Aurometalsaurus](./static/images/content_images/swatch_6C7A89_aurometalsaurus.png) `RGB 108/122/137 | HEX #6C7A89 | NumPy Slate Gray`

![#EEEEEE Isabelline](./static/images/content_images/swatch_EEEEEE_isabelline.png) `RGB 238/238/238 | HEX #EEEEEE | NumPy Cloud Gray`

![#FFC553 Mustard](./static/images/content_images/swatch_FFC553_mustard.png) `RGB 255/197/83 | HEX #FFC553 | NumPy Yellow`

![#FFFFFF White](./static/images/content_images/swatch_FFFFFF_white.png) `RGB 255/255/255 | HEX #FFFFFF | White`


## Deployment

Submit pull requests first, those get run on [Netlify](https://quansight-labs.netlify.app/) and you can see a build preview by clicking on the `details` link at the bottom.

![Build previews](images/readme-build-previews.png)

## Team lists

To update the teams gallery in numpy.org site, you need to run `make teams` Makefile target. It uses the `team_query.py` tool provided by [scientific-python-hugo-theme](https://github.com/scientific-python/scientific-python-hugo-theme). The following pre-requisites need to be met in numpy.org build environment:

* The `team_query.py` tool requires python requests package. Make sure it is installed in your numpy.org build environment before invoking `make teams` Makefile target.

* [GitHub token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with `read:org` permissions is required for requesting numpy.org team data from GitHub. The token has to be exported as `GH_TOKEN`.

```
export GH_TOKEN=xxxxxxxxxx
make teams
```

## Upgrade Hugo

Change the version in `netlify.toml`.

## Analytics

A self-hosted version of [Plausible.io](https://plausible.io) is used to gather simple
and privacy-friendly analytics for the site. The dashboard can be accessed
[here](https://views.scientific-python.org/numpy.org).
