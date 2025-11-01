# main.py — App entry point (final version with menu)

import os
from src.log_analyzer.analyzer import LogAnalyzer
import src.log_generator.generator as gen


class App:
    def __init__(self):
        print("====================================")
        print("Programación multiprocesos en Python")
        print("====================================\n")

    # Create and analyze new log file 

    def create_and_analyze_log(self):
        file_name = input("Introduce el nombre del fichero a crear: ").strip()
        if not file_name:
            print("❌ No has introducido ningún nombre.\n")
            return

        try:
            full_log_path = gen.create_file(file_name)
            print(f"✅ Fichero creado correctamente: {full_log_path}")
        except Exception as e:
            print(f"❌ Error al crear el fichero: {e}\n")
            return

        try:
            analyzer = LogAnalyzer(full_log_path)
            analyzer.load_file()
            analyzer.split_work()
            analyzer.analyze_parallel()
            analyzer.combine_results()

            report_path = analyzer.save_results(out_dir="results")
            print(f"📄 Análisis completo y guardado en: {report_path}\n")

        except Exception as e:
            print(f"❌ Error al analizar el fichero: {e}\n")

    # Analyze existing log

    def analyze_existing_log(self):
        chosen = input("Introduce el nombre del fichero a analizar (sin la extension): ").strip()
        if not chosen:
            print("❌ No has introducido ningun fichero.\n")
            return

        log_path = os.path.join("logs", f"{chosen}.txt")
        if not os.path.exists(log_path):
            print(f"⚠️ Fichero Log no encontrado: {log_path}\n")
            return

        try:
            analyzer = LogAnalyzer(log_path)
            analyzer.load_file()
            analyzer.split_work()
            analyzer.analyze_parallel()
            final_results = analyzer.combine_results()

            print("\n========== Informe final ==========")
            print(f"📁 Fichero: {log_path}")
            print(f"📊 Total de lineas analizadas: {final_results.get('total_lines', len(analyzer.lines))}")

            print("\n🪪 Recuento de tipos de mensajes:")
            for key, value in final_results["messages"].items():
                print(f"  {key}: {value}")

            print("\n🌐 Top 10 IPs más activas:")
            for ip, count in final_results["top_ips"]:
                print(f"  {ip}: {count} times")

            print("\n⏰ Errores por hora:")
            for hour, count in final_results["errors_by_hour"].items():
                print(f"  {hour}:00 -> {count} errors")

            print("===================================")
            print("✅ Análisis completado con éxito!\n")

        except Exception as e:
            print(f"❌ Error analizando el fichero: {e}\n")

    # Menu

    def show_menu(self):
        while True:
            print("========= Menú Principal =========")
            print("1️. Crear nuevo fichero Log y guardarlo")
            print("2️. Analizar un fichero Log ya existente")
            print("3️. Salir")
            print("=============================")

            choice = input("Selecciona una opcion: ").strip()

            if choice == "1":
                self.create_and_analyze_log()
            elif choice == "2":
                self.analyze_existing_log()
            elif choice == "3":
                print("👋 Fin del programa. Hasta pronto!\n")
                break
            else:
                print("⚠️ Opción incorrecta, elige una opcion válida\n")

    # Entry point

    def run(self):
        self.show_menu()


# Run program

if __name__ == "__main__":
    app = App()
    app.run()
