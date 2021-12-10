import os
import sys

# from the sync.soccer directory, run with $ python main.py path/to/data

data_path = sys.argv[1]

game_ids = os.listdir(data_path)
for i, game_id in enumerate(game_ids):

    print('Game', i+1, 'of', len(game_ids))
    print('Syncing game_id:', game_id)
    game_path = os.path.join(data_path, game_id)

    tracab_meta = os.path.join(game_path, f'{game_id}_metadata.xml')
    tracab_data = os.path.join(game_path, f'{game_id}.dat')
    opta_f7  = os.path.join(game_path, 'f7.xml')
    opta_f24 = os.path.join(game_path, 'f24.xml')

    if os.path.isfile(tracab_meta)==False or os.path.isfile(tracab_data)==False or os.path.isfile(opta_f7)==False or os.path.isfile(opta_f24)==False:
        print(game_id, 'does not have all the necessary files for sync')
        print()
        continue

    output_lut = os.path.join(game_path, 'lut.csv')
    output_events = os.path.join(game_path, 'events.csv')
    sync_command = f'stack exec -- sync-soccer {tracab_meta} {tracab_data} {opta_f7} {opta_f24} {output_lut} -e {output_events}'
    print('Executing the following sync command:')
    print(sync_command)
    os.system(sync_command)
    print()
