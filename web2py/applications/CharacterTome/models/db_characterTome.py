# -*- coding: utf-8 -*-

# define the characterTome database
db.define_table('characterInfo',
                Field('image', 'upload'),
                Field('image_1','upload',uploadfield="imageblob"),
                Field('imageblob','blob',default=''),
                Field('name'),
                Field('description'),
                Field('refresh'),
                Field('currRefresh'),
                Field('approach_careful'),
                Field('approach_clever'),
                Field('approach_flashy'),
                Field('approach_forceful'),
                Field('approach_quick'),
                Field('approach_sneaky'),
                Field('stress','integer')
                )
