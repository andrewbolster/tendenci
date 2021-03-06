from tendenci.addons.memberships.models import Notice

def get_membership_notice_choices():
    notice_list = [(0, 'SELECT A NOTICE')]
    notices = Notice.objects.filter(status=True, status_detail='active').order_by('notice_name')
    
    for notice in notices:
        notice_list.append((notice.id, notice.notice_name))
        
    return notice_list 