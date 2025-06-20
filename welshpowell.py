# Pewarnaan graf Surabaya - Welsh Powell terpisah fungsi pengurutan derajat

# List node sesuai V1-V31
nodes = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12',
    'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23',
    'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30', 'V31'
]

# Adjacency list dari graf Surabaya
adjacency = {
    'V1': ['V2','V4','V7','V6','V29'],
    'V2': ['V1','V4','V5','V7'],
    'V3': ['V5','V8','V11','V13'],
    'V4': ['V1','V2'],
    'V5': ['V2','V3','V7'],
    'V6': ['V1','V7','V12','V29'],
    'V7': ['V1','V2','V5','V6','V8'],
    'V8': ['V3','V7','V13','V15'],
    'V9': ['V10','V11','V15'],
    'V10': ['V9','V11','V13'],
    'V11': ['V3','V9','V10','V13'],
    'V12': ['V6','V23','V26'],
    'V13': ['V3','V8','V10','V11'],
    'V14': ['V15','V19','V22'],
    'V15': ['V8','V9','V14','V24','V26'],
    'V16': ['V20','V21','V24','V25'],
    'V17': ['V19','V20'],
    'V18': ['V20','V28'],
    'V19': ['V14','V17','V20','V22'],
    'V20': ['V16','V17','V18','V19','V22'],
    'V21': ['V16','V25','V28','V30'],
    'V22': ['V14','V19','V20'],
    'V23': ['V12','V25','V26','V29'],
    'V24': ['V15','V16','V25','V26'],
    'V25': ['V16','V21','V23','V24','V30'],
    'V26': ['V12','V15','V23','V24'],
    'V27': ['V28'],
    'V28': ['V18','V21','V27','V30'],
    'V29': ['V1','V6','V23','V30','V31'],
    'V30': ['V21','V25','V28','V29','V31'],
    'V31': ['V29','V30']
}

# Nama warna (bisa diubah sesuai kebutuhan)
warna_list = ['Merah', 'Hijau', 'Kuning', 'Biru','Coklat']

# Fungsi untuk mengurutkan node berdasarkan derajat (descending)
def sort_nodes_by_degree(graph):
    degree = {node: len(graph[node]) for node in graph}
    sorted_nodes = sorted(degree, key=
    lambda x: degree[x], reverse=True)
    return sorted_nodes

def welsh_powell(graph):
    sorted_nodes = sort_nodes_by_degree(graph)
    warna_simpul = {}  # dictionary untuk menyimpan warna tiap simpul
    warna_ke = 0  # mulai dari warna ke-0 (Merah)

    while len(warna_simpul) < len(graph):
        dipilih_di_iterasi_ini = []

        for simpul in sorted_nodes:
            if simpul not in warna_simpul:  # simpul belum diberi warna
                bisa_diwarnai = True
                for tetangga in graph[simpul]:
                    if tetangga in warna_simpul and warna_simpul[tetangga] == warna_ke:
                        bisa_diwarnai = False  # tetangga sudah pakai warna ini
                        break
                if bisa_diwarnai:
                    warna_simpul[simpul] = warna_ke
                    dipilih_di_iterasi_ini.append(simpul)

        warna_ke += 1  # ganti warna untuk iterasi berikutnya

        # Cetak hasil iterasi ini
        print("Iterasi ke -", warna_ke, "Warna:", warna_list[warna_ke])
        for simpul in dipilih_di_iterasi_ini:
            print("  Simpul", simpul, "diwarnai", warna_list[warna_ke])
        print()

# Jalankan
welsh_powell(adjacency)
