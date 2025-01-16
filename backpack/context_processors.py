def backpack_context(request):
    backpack = request.session.get('backpack', [])
    return {
        'backpack_count': len(backpack),
    }