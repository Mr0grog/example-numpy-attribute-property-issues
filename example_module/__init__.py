class ExampleClass:
    """
    This is an example of how attributes and attributes that are properties get
    formatted by numpydoc.

    Attributes
    ----------
    normal_attribute : str
        This is a normal attribute, fully specified in class docstring.
    property_attribute
    """

    def __init__(self):
        self.normal_attribute = 'hello'
    
    @property
    def property_attribute(self):
        """
        This attribute is actually a property (i.e. it's actually a function
        call under the hood). The description is pulled from the docstring of
        the method that implements it.

        Returns
        -------
        int
        """
        return len(self.normal_attribute)
