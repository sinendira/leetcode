
class Codec:
    # Initializing our marker
    MARKER = "M"
    
    def serialize_rec(self, node, stream):
        # Adding marker to stream if the node is None
        if node is None:
            stream.append(self.MARKER)
            return

        # Adding node to stream
        stream.append(str(node.val))

        # Doing a pre-order tree traversal for serialization
        self.serialize_rec(node.left, stream)
        self.serialize_rec(node.right, stream)

    def serialize(self, root):
        stream = []
        self.serialize_rec(root, stream)
        # Join the list to create a string with commas separating values
        return ','.join(stream)

    def deserialize_helper(self, values):
        # pop the first element from the list
        val = values.pop(0)

        # Return None when a marker is encountered
        if val == self.MARKER:
            return None

        # Creating new Binary Tree Node from current value from the list
        node = TreeNode(int(val))

        # Doing a pre-order tree traversal for deserialization
        node.left = self.deserialize_helper(values)
        node.right = self.deserialize_helper(values)

        # Return node if it exists
        return node

    def deserialize(self, data):
        values = data.split(',')  # Split the data back into a list
        return self.deserialize_helper(values)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))