class Project:
    def __init__(self, resolve):
        self.obj = resolve.GetProjectManager().GetCurrentProject()

    def __getattr__(self, name):
        """让没有在包装类中定义的属性，直接去内部对象找"""
        return getattr(self.obj, name)

    def __repr__(self):
        """print 时，显示内部对象的 repr"""
        return repr(self.obj)