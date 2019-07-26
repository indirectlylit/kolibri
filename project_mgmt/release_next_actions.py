

class Context():
    def __init__(self, project, collection, version):
        self.project = project
        self.collection = collection
        self.version = version

def create_action(context, title):
    print("A")
    action = context.collection.add_row()
    print("B")
    action.project = context.project
    print("C")
    action.title = title
    print("D")
    action.status = "Not started"
    print("E")
    return action


def stepA_changelog(context):
    title = "{} - update changelog".format(context.version)
    return create_action(context, title)


