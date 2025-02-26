from datetime import date
from datetime import datetime, timedelta

from django.db.models import Sum
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import StudentDaily


@extend_schema(tags=["HeatMapEntity"])
class HeatMapEntityApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        today = date.today()
        today_start = datetime.combine(date.today(), datetime.min.time())
        today_end = datetime.combine(date.today(), datetime.max.time())
        daily_score = StudentDaily.objects.filter(student=user, created_at__range=[today_start, today_end]).aggregate(
            total_score=Sum('task__point'))
        score = daily_score['total_score']
        level = 1
        if score > 20 and score <= 40:
            level = 2
        elif score > 40 and score <= 60:
            level = 3
        elif score > 60 and score <= 80:
            level = 4
        elif score > 80 and score <= 100:
            level = 5
        return Response({
            "pk": user.id,
            "date": today.strftime('%Y-%m-%d'),
            "points": score,
            "lvl": level
        })
