from backend.app.repositories.statistics_repository import StatisticsRepository

repository = StatisticsRepository()

statistics = repository.get_statistics(1208022)

for stat in statistics:
    print(stat)