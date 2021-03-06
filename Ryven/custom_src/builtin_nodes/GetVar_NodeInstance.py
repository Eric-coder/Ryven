from NIENV import *


class GetVar_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(GetVar_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = self.actionmethod ...
        self.var_name = ''
        self.temp_var_val = None

    def update_event(self, input_called=-1):
        if self.input(0) != self.var_name:

            vars_handler = self.flow.parent_script.variables_handler

            if self.var_name != '':  # disconnect old var val update connection
                vars_handler.unregister_receiver(self, self.var_name)

            self.var_name = self.input(0)

            # create new var update connection
            vars_handler.register_receiver(self, self.var_name, M(self.var_val_changed))

            var = vars_handler.get_var(self.input(0))
            if var is not None:
                self.set_output_val(0, var.val)
            else:
                self.set_output_val(0, None)

        else:  # ->> value changed!
            self.set_output_val(0, self.get_var_val(self.var_name))

    def var_val_changed(self, name, val):
        self.update()

    def get_current_var_name(self):
        return self.input(0)

    def get_data(self):
        return {}

    def set_data(self, data):
        pass

    def remove_event(self):
        pass