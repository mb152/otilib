from pyoti import fmod_writer
order = 2
nImBase = 7
w = fmod_writer.writer(nImBase, order, base_name="dual")
w.write_file(tab = '    ', 
            is_std_matmul=True, 
            elemental_feval=True, 
            real_utils=False,
            module_name="hyper_dual")
