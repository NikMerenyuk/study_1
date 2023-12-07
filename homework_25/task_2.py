class RecipeModel:
    def __init__(self, recipe_name: str, author_of_recipe: str, recipe_type: str, recipe_descr: str,
                 link_recipe_video: str, list_of_ingredients: str, kitchen_name: str):
        self.recipe_name = recipe_name
        self.author_of_recipe = author_of_recipe
        self.recipe_type = recipe_type
        self.recipe_descr = recipe_descr
        self.link_recipe_video = link_recipe_video
        self.list_of_ingredients = list_of_ingredients
        self.kitchen_name = kitchen_name


class RecipeView:
    @staticmethod
    def display_recipe(recipe):
        print(f'Recipe name: {recipe.recipe_name};\n'
              f'Author of recipe: {recipe.author_of_recipe};\n'
              f'Recipe type: {recipe.recipe_type};\n'
              f'Recipe description: {recipe.recipe_descr};\n'
              f'Link to the recipe video: {recipe.link_recipe_video};\n'
              f'List of ingredients: {recipe.list_of_ingredients};\n'
              f'Kitchen name: {recipe.kitchen_name}.')


class RecipeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_recipe_name(self, recipe_name):
        self.model.recipe_name = recipe_name

    def set_author_of_recipe(self, author_of_recipe):
        self.model.author_of_recipe = author_of_recipe

    def set_shoes_recipe_type(self, recipe_type):
        self.model.recipe_type = recipe_type

    def set_recipe_descr(self, recipe_descr):
        self.model.recipe_descr = recipe_descr

    def set_shoes_link_recipe_video(self, link_recipe_video):
        self.model.link_recipe_video = link_recipe_video

    def set_shoes_list_of_ingredients(self, list_of_ingredients):
        self.model.list_of_ingredients = list_of_ingredients

    def set_shoes_kitchen_name(self, kitchen_name):
        self.model.kitchen_name = kitchen_name

    def display_recipe(self):
        self.view.display_recipe(self.model)


ingredients = 'flour, baking powder, sugar,salt, milk, egg'
model = RecipeModel('Good Old-Fashioned Pancakes', 'dakota kelly', 'dessert',
                    'I found this pancake recipe in my Grandma\'s recipe book. '
                    'Judging from the weathered look of this recipe card, '
                    'this was a family favorite',
                    'https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/',
                    ingredients, 'USA')
view = RecipeView()
controller = RecipeController(model, view)


if __name__ == '__main__':
    controller.display_recipe()
