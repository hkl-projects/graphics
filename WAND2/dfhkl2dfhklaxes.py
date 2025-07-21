import numpy as np
import pandas as pd
#from tqdm import tqdm

def dfhkl2dfhklaxes(df, min_intensity, factory, geometry, detector, sample, user):
    new_df = pd.DataFrame(columns=['h', 'k', 'l', 'mu', 'omega', 'chi', 'phi', 'gamma','delta', 'd', 'intensity']) 
    engines = factory.create_new_engine_list()
    engines.init(geometry, detector, sample)
    engines.get()
    engine_hkl = engines.engine_get_by_name("hkl")
    engine_hkl.current_mode_set('lifting_detector_mu') # TODO CHECK THIS
    #axes = geometry.axis_names_get()
    #for axis in axes:
    #    tmp = geometry.axis_get(axis)
    #    #if (axis=='omega') or (axis=='chi') or (axis=='phi'):
    #    if (axis=='chi'):
    #        tmp.min_max_set(-0.01, 0.01, user)
    #        geometry.axis_set(axis, tmp)
    num_refl = len(df)
    print(f"Searching through {num_refl} reflections...")
    found = 0
    not_found = 0
    #for idx, refl in tqdm(df.iterrows(), total=num_refl, desc=Reflections):
    for idx, refl in df.iterrows():
        h = refl['h']
        k = refl['k']
        l = refl['l']
        d = refl['d']
        inten = refl['intensity']
        if inten > min_intensity:
            try:
                solutions = engine_hkl.pseudo_axis_values_set([h,k,l], user)
                # similar to apply_axes_solns in hkl.py
                for i, item in enumerate(solutions.items()):
                    read = item.geometry_get().axis_values_get(user)
                    if read is not None:
                        new_row = pd.DataFrame([{'h':h, \
                                                'k':k, \
                                                'l':l, \
                                                'd':4.5, \
                                                'intensity':inten, \
                                                'mu':read[0], \
                                                'omega':read[1], \
                                                'chi':read[2], \
                                                'phi':read[3], \
                                                'gamma':read[4], \
                                                'delta':read[5]}])
                        if new_row is not None:
                            new_df = pd.concat([new_df, new_row], ignore_index=True)
                            found += 1
            except Exception as e:
                not_found += 1
                print(e)
    print(f"found motor positions for {found} reflections. Did not find for {not_found} reflections.")
    return new_df
