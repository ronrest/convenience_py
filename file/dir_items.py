import os

# ==============================================================================
#                                                                      DIR ITEMS
# ==============================================================================
def dir_items(d, opt="all", rel=True, root="", filter=""):
    """ Takes a directory path (as a string). And returns the paths/names of
        the items that are contained in that directory.
    
        ALL ITEMS, DIRECTORIES, OR JUST FILES
        ----------------------------
        Depending on the options you use, you can return:
         - a list of ALL the items (opt="all")
         - just the subdirectories (opt="dirs")
         - only files (opt="files")
         - directories and files as tuple of two separate lists (opt="grouped")
    
        RELATIVE OR ABSOLUTE PATHS
        ----------------------------
        The items can be returned as:
         - just the filenames of the items (rel=True)
         - the absolute path to the items (rel=False)
         - the path to the items relative to any directory whatsoever in the
           entire system filestructure (rel=True, root="some/dir/")
    
        STRING FILTERS
        ----------------------------
        You can also specify to only return items where the filename contains
        some specified text, eg, only return items containing ".jpg"
    
    
        NOTE
        ----------------------------
        The items are not returned in any particular order.
    
    Args:
        d: (str)
            The full path to the directory you want to search in.
        opt: (str or None) {default = "all"}
            The option to use:
    
            "dirs" : return just the subdirectories
            "files": return just the files
            "all"  : return all items
            "grouped" : returns a tuple of two lists. ([directories], [files])
    
        rel: (optional)(boolean)
            if True, then it returns the listed items as directories relative
            to the d directory.
    
            IF False, then it returns the FULL paths.
        
        root: (Optional)(str)
            A directory path that we want to use as the root for relative paths.
            If left blank, then it uses the directory set in d as the root
            directory.
        
        filter: (string)
            Used to filter for items that contain this string in their name.

    Returns:
        See notes in description.
    """
    # ==========================================================================
    # TODO: Expand the filter, so you can filter using regex, file extensions,
    #       or mime types
    # TODO: sort!!! perform sorting (NOTE: that using list.sort() is a bad idea,
    #       because it sorts by ascii order not alphabetical order.

    # --------------------------------------------------------------------------
    #                                                                      Setup
    # --------------------------------------------------------------------------
    fList = []  # file List
    dList = []  # Directory List
    d = os.path.abspath(d)  # desired directory as an absolute path

    # --------------------------------------------------------------------------
    #       Set the ralative/absolute path to append to the output list of items
    # --------------------------------------------------------------------------
    if rel:
        root = root.strip()
        if  root == "":
            root = d
        outpath = os.path.relpath(d, root)
    else:
        outpath = d

    # if the root path is d, then remove the "." from path.
    if outpath == ".":
        outpath = ""

    # --------------------------------------------------------------------------
    #          Sort each item in the directory into either a directory or a file
    # --------------------------------------------------------------------------
    for item in os.listdir(d):
        # If item doesnt satisfy our filter condition then skip to the next item
        if filter not in item:
            continue

        full_item_path = os.path.join(d, item)      # Full path to the item
        out_item_path = os.path.join(outpath, item) # Path used in output list

        if os.path.isfile(full_item_path):
            fList.append(out_item_path)
        elif os.path.isdir(full_item_path):
            dList.append(out_item_path)
        else:
            print "WARNING: directoryItems found an item that is neither a \n"\
                  "         file, nor a directory"

    # --------------------------------------------------------------------------
    #                                                      Return the item lists
    # --------------------------------------------------------------------------
    if (opt is None) or (opt.lower() in ["none", "", "all"]):
        return dList + fList
    elif opt.lower() in ["file", "files", "f"]:
        return fList
    elif opt.lower() in ["dir", "dirs", "d", "folder", "folders"]:
        return dList
    elif opt.lower() in ["grouped", "group", "g"]:
        return (dList, fList)
    else:
        msg = "\n    dir_items(): the only valid values for the `opt` argument" \
              "\n    are 'all', 'dirs', 'files', and 'grouped'"
        raise ValueError(msg)

