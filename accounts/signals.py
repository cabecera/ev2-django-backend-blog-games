def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from django.apps import apps

    try:
        Model = apps.get_model('core', 'PostProduct')
    except LookupError:
        return

    ct = ContentType.objects.get_for_model(Model)

    # crear permisos si no existen y grupos
    perms = {
        'add_postproduct': Permission.objects.get_or_create(codename='add_postproduct', content_type=ct)[0],
        'change_postproduct': Permission.objects.get_or_create(codename='change_postproduct', content_type=ct)[0],
        'delete_postproduct': Permission.objects.get_or_create(codename='delete_postproduct', content_type=ct)[0],
        'view_postproduct': Permission.objects.get_or_create(codename='view_postproduct', content_type=ct)[0],
    }

    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')

    editors.permissions.add(perms['add_postproduct'], perms['change_postproduct'], perms['delete_postproduct'], perms['view_postproduct'])
    viewers.permissions.add(perms['view_postproduct'])
