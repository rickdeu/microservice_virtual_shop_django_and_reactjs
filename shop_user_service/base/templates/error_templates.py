class ErrorTemplate:

    class AuthorizedError:
        UNAUTHORIZED = "Incorrect authentication credentials."

    class CategoryError:
        CATEGORY_NOT_FOUND = "Category not found."

        CAN_NOT_DELETE_CATEGORY = "You can't delete this category because it has subcategories."

        CATEGORY_IS_ALREADY_DELETED = "Category is already deleted."

    class SubCategoryError:
        SUB_CATEGORY_NOT_FOUND = "Subcategory not found."

        CAN_NOT_DELETE_SUB_CATEGORY = "You can't delete this subcategory because it has products."

        SUB_CATEGORY_IS_ALREADY_DELETED = "Subcategory is already deleted."

    class ProductError:
        PRODUCT_NOT_FOUND = "Product not found."

        PRODUCT_IS_ALREADY_DELETED = "Product is already deleted."

    class ProductImageError:
        PRODUCT_IMAGE_NOT_FOUND = "Product image not found."

        PRODUCT_IMAGE_IS_ALREADY_DELETED = "Product image is already deleted."

    class StoreError:
        STORE_NOT_FOUND = "Store not found."

        STORE_IS_ALREADY_DELETED = "Store is already deleted."

    class CustomerError:
        CUSTOMER_NOT_FOUND = "Customer not found."

        CUSTOMER_IS_ALREADY_DELETED = "Customer is already deleted."
