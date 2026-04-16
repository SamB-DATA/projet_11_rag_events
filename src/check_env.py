from importlib import import_module

REQUIRED_PACKAGES = [
    "pandas",
    "numpy",
    "faiss",
    "langchain",
    "langchain_community",
    "langchain_mistralai",
    "mistralai",
    "dotenv",
    "requests",
]


def main():
    failed = []

    for package in REQUIRED_PACKAGES:
        try:
            import_module(package)
            print(f"[OK] {package}")
        except Exception as e:
            failed.append((package, str(e)))
            print(f"[ERREUR] {package} -> {e}")

    if failed:
        print("\n❌ Environnement invalide")
    else:
        print("\n✅ Environnement valide")


if __name__ == "__main__":
    main()