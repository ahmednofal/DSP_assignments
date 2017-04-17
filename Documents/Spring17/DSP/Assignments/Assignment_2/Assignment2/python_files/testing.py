import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
from signal_file import signal__
from datautils import load_wav_file, write_wav_file

# cell 1
reconstructed = 'recpnstructed '
local_path = '/home/naufal/Documents/Spring17/DSP/Assignments/Assignment_2/'
recorded_wav_folder = 'WAV_Files/recorded/'
reconstructed_wav_folder = 'WAV_Files/reconstructed/'
recorded_wav_file = 'ahmednofal_8khz_32bitfloatPCM'
reconstructed_wav_file = recorded_wav_file + reconstructed
save_figures_path = local_path + 'Figures2/'
real_part = save_figures_path + 'real_part'
imag_part = save_figures_path + 'imag_part'
phase_part = save_figures_path + 'phase_part'
magnitude_part = save_figures_path + 'magnitude_part'
discrete_signal_file_path = save_figures_path + 'discrete_signal'
reconstructed_signal_file_path = save_figures_path + 'reconstructed_signal_256'
file_format = '.pdf'
audio_file_format = '.wav'
discrete_signal = 'Discrete Signal'

# # number of samples for the signal
# samplesNum = 256
# # DftPointsNum = 256
# samplingRate = 2
#
# #Generating the signal x and y values
# discrete_signal_obj = signal__()
# continuous_signal_amp_values, continuous_signal_samples_idx = discrete_signal_obj.GenerateSignal(n=samplesNum,
#                                                                                                  fs=samplingRate)
#
# print (continuous_signal_amp_values)
# print (continuous_signal_samples_idx)
# # plotting the signal
#
# plt.suptitle(discrete_signal)
# plt.xlabel('n')
# plt.ylabel('amplitude')
#
# plt.plot(continuous_signal_samples_idx, continuous_signal_amp_values)
# # displaying the signal
#
# savefig(discrete_signal_file_path + file_format, bbox_inches='tight')
# plt.show()
# plt.clf()
# # cell 2
#
# # trying out the 256 Point DFT
# # cell 2
#
# # trying out the 256 Point DFT
# DFT_points_num_arr = [256, 128]
# processed_signal = signal__()
#
# for DftPointsNum in DFT_points_num_arr:
#     processed_signal.__init__()
#     processed_signal.GenerateSignal(n=DftPointsNum, fs=samplingRate)
#     dft_amplitude_values, frequencyAxis_values = processed_signal.calculate_dft(samplingRate=samplingRate,
#                                                                                 DftPointsNum=DftPointsNum,
#                                                                                 samplesNum=DftPointsNum)
#
#     plt.suptitle('real values DFT Points Number = ' + str(DftPointsNum))
#     plt.xlabel('m')
#     plt.ylabel('real part of X[m]')
#
#     plt.plot(frequencyAxis_values, dft_amplitude_values.real)
#     savefig(real_part + str(DftPointsNum) + file_format, bbox_inches='tight')
#     plt.show()
#     plt.clf()
#
#     plt.suptitle('imag values DFT Points Number = ' + str(DftPointsNum))
#     plt.xlabel('m')
#     plt.ylabel('imaginary part of X[m]')
#
#     plt.plot(frequencyAxis_values, dft_amplitude_values.imag)
#
#     savefig(imag_part + str(DftPointsNum) + file_format, bbox_inches='tight')
#     plt.show()
#     plt.clf()
#
#     angle_values, magnitude_values = processed_signal.to_polar()
#
#     plt.suptitle('phase part DFT Points Number = ' + str(DftPointsNum))
#     plt.xlabel('m')
#     plt.ylabel('phase shift of X[m]')
#
#     plt.plot(frequencyAxis_values, angle_values)
#     savefig(phase_part + str(DftPointsNum) + file_format, bbox_inches='tight')
#     plt.show()
#     plt.clf()
#
#     plt.suptitle('magnitude part DFT Points Number = ' + str(DftPointsNum))
#     plt.xlabel('m')
#     plt.ylabel('magnitude of X[m]')
#
#     plt.plot(frequencyAxis_values, magnitude_values)
#     savefig(magnitude_part + str(DftPointsNum) + file_format, bbox_inches='tight')
#     plt.show()
#
#     if DftPointsNum == 256:
#         reconstructed_signal_amplitude_values, reconstructed_signal_x_axis_values = processed_signal.calculate_idft()
#         # print(reconstructed_signal_amplitude_values)
#         plt.clf()
#         plt.suptitle('reconstructed signal')
#         plt.xlabel('n')
#         plt.ylabel('amplitude')
#         plt.plot(reconstructed_signal_x_axis_values, reconstructed_signal_amplitude_values)
#         savefig(reconstructed_signal_file_path + file_format, bbox_inches='tight')
#         plt.show()
# #

print('\t\tTesting the wav file recorded\n')
rate, data = load_wav_file(local_path + recorded_wav_folder + recorded_wav_file + audio_file_format)
audio_signal_samples_num = data.shape[0]
audio_signal = signal__()
audio_signal.generated_signal = True
audio_signal.continuousSignal = data
audio_signal.samplingRate = rate
audio_signal.samplesNum = audio_signal_samples_num
audio_signal.calculate_dft(samplingRate=17000,  DftPointsNum=audio_signal_samples_num,
                           samplesNum=audio_signal_samples_num)
wav_file_reconstructed_data, wav_file_samples_idx = audio_signal.calculate_idft()
print("wavfile reconstructed data ", wav_file_reconstructed_data, "\n")
print("rate is ", rate)
print("audio signal idft is :  ", audio_signal.idft)




write_wav_file(filename=local_path + reconstructed_wav_folder + reconstructed_wav_file + audio_file_format, rate=rate, data=wav_file_reconstructed_data.real)

