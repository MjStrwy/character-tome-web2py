# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    all_characterSheets = db(db.characterInfo.id > 0).select()
    fateLadder = dict(
                            [
                                (-2, 'terrible (-2)'),
                                (-1, 'poor (-1)'),
                                (0, 'mediocre (+0)'),
                                (1, 'average (+1)'),
                                (2, 'fair (+2)'),
                                (3, 'good (+3)'),
                                (4, 'great (+4)'),
                                (5, 'superb (+5)'),
                                (6, 'fantastic (+6)'),
                                (7, 'epic (+7)'),
                                (8, 'legendary (+8)')
                            ]
                        )
    return locals()


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
