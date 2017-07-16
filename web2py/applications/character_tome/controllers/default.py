# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    characters = db().select(db.characters.ALL, orderby=db.characters.name)
    return dict(characters=characters)

def show():
    character = db.characters(request.args(0, cast=int)) or redirect(URL('index'))
    
    db.aspects.character_id.default = character.id
    aspects_form = SQLFORM(db.aspects)
    if aspects_form.process().accepted:
        response.flash = 'You\'ve added an Aspect!'
    aspects = db(db.aspects.character_id == character.id).select()
    
    db.stunts.character_id.default = character.id
    stunts_form = SQLFORM(db.stunts)
    if stunts_form.process().accepted:
        response.flash = 'You\'ve added a Stunt!'
    stunts = db(db.stunts.character_id == character.id).select()
    
    fate_ladder = {-2: 'Terrible, -2', -1: 'Poor, -1', 0: 'Mediocre, 0', 1:'Average, +1', 2:'Fair, +2', 3:'Good, +3', 4:'Great, +4', 5:'Superb, +5', 6:'Fantastic, +6', 7:'Epic, +7', 8:'Legendary, +8'}
    
    return dict(character=character, aspects=aspects, aspects_form=aspects_form, stunts=stunts, stunts_form=stunts_form, fate_ladder=fate_ladder)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
