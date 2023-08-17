class ErrorTemplate:

    class AuthorizedError:
        UNAUTHORIZED = "Incorrect authentication credentials."

    class CategoryError:
        CATEGORY_NOT_FOUND = "Category not found."

        CAN_NOT_DELETE_CATEGORY = "You can't delete this category because it has products"

        CATEGORY_IS_ALREADY_DELETED = "Category is already deleted."

    class ProductError:
        PRODUCT_NOT_FOUND = "Product not found."

        PRODUCT_IS_ALREADY_DELETED = "Product is already deleted."