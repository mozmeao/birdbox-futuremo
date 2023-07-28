# Birdbox

A system to create a quick-deploy, easily customisable, CMS-backed microsite service

STATUS: Very much WIP

LICENSE: [Mozilla Public License Version 2.0](LICENSE)

----

## Running locally, for development

* Install the `just` taskrunner (Docs [here](https://github.com/casey/just); spoiler: `brew install just`)
* Check out the repo
* `cd` path/to/birdbox
* Create then activate a virtual environment (pyenv + pyenv-virtualenv is recommended, but not required - see [Bedrock docs](https://bedrock.readthedocs.io/en/latest/install.html#local-installation) for an example)
* `just preflight` to install Python and JS dependencies, run migrations (against a simple SQLite DB for local dev), create a cache table
* To make an admin user `just createsuperuser`
* To run the local webpack bundler + django runserver: `just run-local` or `npm start` (both do the same thing)

Docker version: TO COME

Main Wagtail admin/editor docs are at https://guide.wagtail.org/en-latest/

Deployment/actual use instructions: TO COME


----
## How To: Add a new StreamField component based on a Protocol component

(This assumes you know your way around Wagtail - if not, please at least review the [Wagtail quick start](https://docs.wagtail.org/en/stable/getting_started/index.html))

1. Define a new block in Python in `microsite/blocks.py` with the fields/content items that the Protocol component needs (eg title, description, image)
2. Add a new HTML template fragment for the new block in `microsite/templates/blocks/`
    * Base the markup on the HTML in the Protocol docs' examples
    * Remember to circle back and reference the template in the Python block definition
3. If JS or CSS is needed for the component, configure webpack to build it - see `src/css/protocol/card.scss` as an example
    * Remember to circle back to the Python nlock definition to set the `frontend_media` property so that this CSS/JS gets included when needed
4. Find the page (in `microsite.models`) with a StreamField that you want the new component to be available in. Add it to the list of blocks that are available.
5. `make makemigrations` then `make migrate` to get the DB up to speed
6. In the Wagtail CMS admin, amend an instance of the relevant page to use your new block - you should be able to see it in the live preview. Usually it takes a bit of tweaking to get the page to look as you intend.
7. If you need to add custom CSS to override what's in Protocol, add to `src/css/birdbox-protocol-overrides.css`

----

