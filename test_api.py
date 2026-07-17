from backend.app.services.match_context_service import MatchContextService

service = MatchContextService()

context = service.build(
    "Liverpool",
    "Chelsea"
)

print(context)