from art.project import ArtProject

from .dataset import MyDataModule
from .models.base_model import Model


def main():
    data_module = MyDataModule()
    model = Model
    project = ArtProject("plot_project", data_module)
    project.add_step(...)
    project.run_all()


if __name__ == "__main__":
    main()
