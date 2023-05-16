phones_db: list[dict] = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def main(phones_db: list[dict]) -> str:

    sales_pcs: int = 0
    total_avg_sales: int = 0

    for phone in phones_db:

        total_sales_by_brand: int = sum(phone['items_sold'])
        avg_sales: int = total_sales_by_brand // len(phone['items_sold'])
        sales_pcs += total_sales_by_brand
        total_avg_sales += len(phone['items_sold'])

        print(f"{phone['product']} sold: {total_sales_by_brand} pcs.")
        print(f"{phone['product']} average month sales: {avg_sales} pcs.")

    print(f'Total sales: {sales_pcs} pcs.')
    print(f'Total average sales: {sales_pcs // total_avg_sales} pcs.')


if __name__ == "__main__":
    main(phones_db)
