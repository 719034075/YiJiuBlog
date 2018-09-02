from apps.catalog.models import Catalog

catalog = Catalog.query.order_by(Catalog.name).all()

print(catalog)
