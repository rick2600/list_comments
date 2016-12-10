from binaryninja import *


def do_formatting(comment):
    return comment.replace("\n", "\\n")

def list_comments(bv):
    all_comments = []
    for func in bv.functions:
        for address, comment in func.comments.iteritems():
            content = "0x%x    %s" %(int(address), do_formatting(comment))
            all_comments.append(content)
           
    show_plain_text_report("List Comments", "\n".join(all_comments))

PluginCommand.register("List Comments", "List all comments", list_comments)
