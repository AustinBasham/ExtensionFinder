# ExtensionFinder
Script to find details about web extensions
Only works for Windows Chrome right now. Looking to add Opera, Opera GX, Firefox and Edge. As well as a powershell variant.

Takes user input to determine which user to search for as part of the user path. Lists the ext name, ext id, ext ver and creation date of the ext id folder in a csv. Saves the csv in the pwd. Several extension id's are hard coded because the name in the manifest file isn't readable and they're builtin or default with chrome.

If the version number is very high (for example 30) on a Google extension check for something like ABCsoup.
