
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import urllib
import os

# TODO: take into account relative URLS.

# ==============================================================================
#                                                       DOWNLOAD_LINKS_FROM_PAGE
# ==============================================================================
def download_links_from_page(page, extension="", output_dir="", ltf=False,
                             base_url=""):
    """
    Downloads files from some html page. you can specify that you only want
    files with a particular extension, and where to save them.

    NOTE: Currently it does not support downloading of files that are listed
    as relative links.

    :param page:
        either a url, or the contents of an html page.

    :param extension:
        extension of file you want to download, eg "pdf".
        If left blank, it will download ALL links on the page.
    :param output_dir:
        what directory to save files to
    :param ltf:
        Link Text as Filename

        If True Use the link text as the file name. Replacing any spaces with
        underscores.

        If false, it uses the original remote file name.
    :param base_url:
        This is only used if `page` is not a url.

        If page is a string containing the HTML content, then it is a good idea
        to specify the base directory that the page come from. Without it, any
        relative file paths to files in links will fail to download.
    """
    # Creates the directory if it does not already exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Automatically detect if the content is a HTTP URL, if so, download the
    # html page content. otherwise treat 'page' as an html page.
    # Get the html content from the url specified
    url_was_provided = True if re.search("^(https://|http://)", page) else False
    if url_was_provided:
        html = urllib2.urlopen(page)
        base_url = os.path.split(page)[0]
    else:
        html = page

    soup = BeautifulSoup(html)

    # Returns all links
    if extension != "":
        links = soup.findAll('a',
                             attrs={'href': re.compile(".{}$".format(extension))})
    else:
        links = soup.findAll('a')

    # ------------------------------------------------------------------------------
    #                                                   DOWNLOAD EACH FILE AT A TIME
    # ------------------------------------------------------------------------------
    unprocessed_links = []  # keep a list of files that could not be downloaded
    for link in links:
        link_url = link["href"]

        # Determine if it's an absolute path to a file  using http or https file
        full_url = True if re.search("^(https://|http://)", link_url) else False

        # Use base_url to convert to a full path if link_url is a relative path
        link_url = link_url if full_url else os.path.join(base_url, link_url)

        # --------------------------------------------------------------------------
        # Extract the link test to use as the file name, otherwise use the remote
        # filename
        # --------------------------------------------------------------------------
        if ltf:
            filename = (link.contents[0]).replace(" ", "_") + "." + extension
        else:
            filename = os.path.split(link_url)[1]

        # --------------------------------------------------------------------------
        #                                                          Download the file
        # --------------------------------------------------------------------------
        try:
            print("Downloading " + link_url)
            urllib.urlretrieve(link_url, os.path.join(output_dir, filename))
            print("--done")
        except:
            print("Could NOT download " + link_url)
            unprocessed_links.append(link_url)

    print("Done Downloading Files")
    if len(unprocessed_links) > 0:
        print("The following could NOT be downloaded" + "\n    ".join([""] + a))

# download_links_from_page(url, extension="jpg", output_dir="/tmp/mydir", ltf=False)