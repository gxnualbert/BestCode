from django.shortcuts import render

def activity(request):
    context = {
        'nav_items': [{'path': 'activities', 'text': '活动'}],
        'registered': False,
        'candidates': [
            {"photo": "main/images/baqizhao.jpg",
			"code_desc": "经过评委合议，2016年Q4最佳代码评选结果新鲜出炉，最佳代码获得者为Moon（刘轶材）和Nero（刘雍琪），恭喜两位！同时，也感谢其他参选者的积极参与和各部门对本>活动的大力支持！",
            "vote_count": "100",
            "praise_count": "100",
            "comment_count": "843",
            "browse_times": "1024"},
            {"photo": "main/images/baqizhao.jpg",
			"code_desc": "经过评委合议，2016年Q4最佳代码评选结果新鲜出炉，最佳代码获得者为Moon（刘轶材）和Nero（刘雍琪），恭喜两位！同时，也感谢其他参选者的积极参与和各部门对本>活动的大力支持！",
            "vote_count": "100",
            "praise_count": "100",
            "comment_count": "843",
            "browse_times": "1024"},
            {"photo": "main/images/baqizhao.jpg",
			"code_desc": "经过评委合议，2016年Q4最佳代码评选结果新鲜出炉，最佳代码获得者为Moon（刘轶材）和Nero（刘雍琪），恭喜两位！同时，也感谢其他参选者的积极参与和各部门对本>活动的大力支持！",
            "vote_count": "100",
            "praise_count": "100",
            "comment_count": "843",
            "browse_times": "1024"},
            {"photo": "main/images/baqizhao.jpg",
			"code_desc": "经过评委合议，2016年Q4最佳代码评选结果新鲜出炉，最佳代码获得者为Moon（刘轶材）和Nero（刘雍琪），恭喜两位！同时，也感谢其他参选者的积极参与和各部门对本>活动的大力支持！",
            "vote_count": "100",
            "praise_count": "100",
            "comment_count": "843",
            "browse_times": "1024"},
            {"photo": "main/images/baqizhao.jpg",
			"code_desc": "经过评委合议，2016年Q4最佳代码评选结果新鲜出炉，最佳代码获得者为Moon（刘轶材）和Nero（刘雍琪），恭喜两位！同时，也感谢其他参选者的积极参与和各部门对本>活动的大力支持！",
            "vote_count": "100",
            "praise_count": "100",
            "comment_count": "843",
            "browse_times": "1024"},
            {"photo": "main/images/baqizhao.jpg",
			"code_desc": "经过评委合议，2016年Q4最佳代码评选结果新鲜出炉，最佳代码获得者为Moon（刘轶材）和Nero（刘雍琪），恭喜两位！同时，也感谢其他参选者的积极参与和各部门对本>活动的大力支持！",
            "vote_count": "100",
            "praise_count": "100",
            "comment_count": "843",
            "browse_times": "1024"},
        ],
    }
    return render(request, 'activities/activity.html', context)	
