import psycopg2

#PostgreSQL 연결 설정
connection = psycopg2.connect(
    port="5432",
    user="postgres",
    password="1111"
)




def insert_detail_page(detail_page_obj):
    #file_path = f'C:\\Users\\USER\\Downloads\\{file_name}', file_path = f'C:\\Users\\PC\\Downloads\\{file_name}'
    file_path = f'C:\\Users\\USER\\Downloads\\{detail_page_obj.file_data_name}.zip'
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
    except FileNotFoundError:
        print("다운로드한 파일이 없습니다.")
        file_data = ''
    with connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO public.detail (
                        file_data_name, classification_system, providing_agency, department_name,
                        department_phone_number, basis_of_possession, collection_method, update_period,
                        next_registration_date, media_type, total_rows, extension, keywords,
                        cumulative_downloads, download_shortcut, registration_date, modification_date,
                        data_limit, provided_form, description, url, other_notes, cost_assessment,
                        cost_basis_and_unit, usage_permission_range, file
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                ) RETURNING id
            """, (detail_page_obj.file_data_name, detail_page_obj.classification_system, detail_page_obj.providing_agency, detail_page_obj.department_name,
                        detail_page_obj.department_phone_number, detail_page_obj.basis_of_possession, detail_page_obj.collection_method, detail_page_obj.update_period,
                        detail_page_obj.next_registration_date, detail_page_obj.media_type, detail_page_obj.total_rows, detail_page_obj.extension, detail_page_obj.keywords,
                        detail_page_obj.cumulative_downloads, detail_page_obj.download_shortcut, detail_page_obj.registration_date, detail_page_obj.modification_date,
                        detail_page_obj.data_limit, detail_page_obj.provided_form, detail_page_obj.description, detail_page_obj.url, detail_page_obj.other_notes, detail_page_obj.cost_assessment,
                        detail_page_obj.cost_basis_and_unit, detail_page_obj.usage_permission_range, file_data))
        connection.commit()
        detail_pk_id = cursor.fetchone()[0]
        return detail_pk_id
    

def insert_main_page(title, content, provider, date, view, download, periodic_data, keywords_str):
    with connection, connection.cursor() as cursor:
        cursor.execute("INSERT INTO public.main (title, content, provider, date, view, download, periodic_data, keywords_str) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id", (title, content, provider, date, view, download, periodic_data, keywords_str))
        connection.commit()
        main_pk_id = cursor.fetchone()[0]
        return main_pk_id
    
def insert_main_detail_relation(main_id, detail_id):
    with connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO public.main_detail_relation (main_id, detail_id)
            VALUES (%s, %s)
        """, (main_id, detail_id))
        connection.commit()    
