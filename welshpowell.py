# Pewarnaan graf Surabaya - Welsh Powell terpisah fungsi pengurutan derajat

# List node sesuai V1-V31
nodes = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12',
    'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23',
    'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30', 'V31'
]

# Adjacency list dari graf Surabaya
adjacency = {
    'V1': ['V2', 'V23', 'V7', 'V6', 'V29'],
    'V2': ['V4', 'V1', 'V5', 'V7'],
    'V3': ['V5', 'V13', 'V11'],
    'V4': ['V2'],
    'V5': ['V2', 'V3', 'V7', 'V13', 'V8'],
    'V6': ['V1', 'V8', 'V12', 'V7'],
    'V7': ['V2', 'V1', 'V5', 'V6'],
    'V8': ['V13', 'V15', 'V6', 'V12', 'V10', 'V5'],
    'V9': ['V10', 'V14', 'V15'],
    'V10': ['V11', 'V8', 'V9', 'V13', 'V15'],
    'V11': ['V3', 'V13', 'V10'],
    'V12': ['V1', 'V6', 'V8', 'V15', 'V26', 'V23', 'V24'],
    'V13': ['V3', 'V8', 'V11', 'V10', 'V5'],
    'V14': ['V15', 'V22', 'V9'],
    'V15': ['V8', 'V9', 'V14', 'V22', 'V16', 'V12', 'V26', 'V10'],
    'V16': ['V20', 'V21', 'V26', 'V24', 'V18', 'V15', 'V22'],
    'V17': ['V19', 'V22'],
    'V18': ['V20', 'V27', 'V21', 'V16'],
    'V19': ['V17', 'V20', 'V22'],
    'V20': ['V18', 'V19', 'V22', 'V16'],
    'V21': ['V16', 'V18', 'V25', 'V24', 'V28', 'V25'],
    'V22': ['V14', 'V19', 'V20', 'V17', 'V15', 'V16'],
    'V23': ['V12', 'V24', 'V29', 'V1', 'V30'],
    'V24': ['V26', 'V16', 'V25', 'V30', 'V21', 'V12', 'V23'],
    'V25': ['V21', 'V16', 'V24', 'V30', 'V28'],
    'V26': ['V24', 'V16', 'V15', 'V12'],
    'V27': ['V28', 'V18', 'V21'],
    'V28': ['V27', 'V21', 'V25', 'V30'],
    'V29': ['V1', 'V23', 'V30'],
    'V30': ['V29', 'V23', 'V24', 'V25', 'V28'],
    'V31': ['V25', 'V30', 'V28']
}

# Nama warna (bisa diubah sesuai kebutuhan)
warna_list = ['', 'Hijau', 'Kuning', 'Biru','Coklat','Merah']

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
