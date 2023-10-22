-- make 20 fake users
INSERT INTO users (id, user_name, team) 
VALUES (1, 'John', 0), (2, 'Robert', 0), (3, 'Lee', 0), (4, 'Alice', 0), (5, 'Jane', 0), (6, 'Wanda', 1), (7, 'Abigail', 1), (8, 'Yeric', 1), (9, 'Nicholas', 1), (10, 'Joshua', 1), (11, 'James', 0), (12, 'Henry', 0), (13, 'Andrew', 0), (14, 'Thomas', 0), (15, 'Samuel', 0), (16, 'Daniel', 1), (17, 'David', 1), (18, 'Joseph', 1), (19, 'Matthew', 1), (20, 'Anthony', 1);

-- insert form responses for each user for the past few days
INSERT INTO form_responses (user_id, score, sending_time)
VALUES 
(1,0.9323428368617406, DATE('now', '-7 days')),
(2,0.7451917880774135, DATE('now', '-7 days')),
(3,0.9009414546936381, DATE('now', '-7 days')),
(4,0.8968845007384237, DATE('now', '-7 days')),
(5,0.7524505764759714, DATE('now', '-7 days')),
(6,0.992154799138101, DATE('now', '-7 days')),
(7,0.8593667946354892, DATE('now', '-7 days')),
(8,0.7433709244679139, DATE('now', '-7 days')),
(9,0.7961683401254392, DATE('now', '-7 days')),
(10,0.7804251612794174, DATE('now', '-7 days')),
(11,0.9163213639912587, DATE('now', '-7 days')),
(12,0.7494234258028338, DATE('now', '-7 days')),
(13,0.9794552291941486, DATE('now', '-7 days')),
(14,0.9524803705012121, DATE('now', '-7 days')),
(15,0.253423523423423, DATE('now', '-7 days')),
(16,0.795112926575699, DATE('now', '-7 days')),
(17,0.9338288871145974, DATE('now', '-7 days')),
(18,0.8255744565616209, DATE('now', '-7 days')),
(19,0.8281860646158865, DATE('now', '-7 days')),
(20,0.8327671375580419, DATE('now', '-7 days')),
(1,0.9073203446231661, DATE('now', '-6 days')),
(2,0.9663806228398438, DATE('now', '-6 days')),
(3,0.8575804175279425, DATE('now', '-6 days')),
(4,0.8953097942627172, DATE('now', '-6 days')),
(5,0.8688408239378731, DATE('now', '-6 days')),
(6,0.7452011828169739, DATE('now', '-6 days')),
(7,0.7410249528868825, DATE('now', '-6 days')),
(8,0.8693902872072992, DATE('now', '-6 days')),
(9,0.8750395564321252, DATE('now', '-6 days')),
(10,0.9880617345519445, DATE('now', '-6 days')),
(11,0.9506665024800278, DATE('now', '-6 days')),
(12,0.9300921969467935, DATE('now', '-6 days')),
(13,0.9367515974588225, DATE('now', '-6 days')),
(14,0.9648090750622302, DATE('now', '-6 days')),
(15,0.05345323423423, DATE('now', '-6 days')),
(16,0.9478965904595158, DATE('now', '-6 days')),
(17,0.8683241335411539, DATE('now', '-6 days')),
(18,0.9383704402437838, DATE('now', '-6 days')),
(19,0.9804214727505562, DATE('now', '-6 days')),
(20,0.8463087299992254, DATE('now', '-6 days')),
(1,0.7351507395619179, DATE('now', '-5 days')),
(2,0.8800811034754243, DATE('now', '-5 days')),
(3,0.8033128152672345, DATE('now', '-5 days')),
(4,0.7725011011900053, DATE('now', '-5 days')),
(5,0.9363444542915389, DATE('now', '-5 days')),
(6,0.8450018812774712, DATE('now', '-5 days')),
(7,0.8736551541991779, DATE('now', '-5 days')),
(8,0.7472272036755295, DATE('now', '-5 days')),
(9,0.7085962623961527, DATE('now', '-5 days')),
(10,0.7523070159820969, DATE('now', '-5 days')),
(11,0.8856162835579904, DATE('now', '-5 days')),
(12,0.9532690533188741, DATE('now', '-5 days')),
(13,0.8422938221089322, DATE('now', '-5 days')),
(14,0.8816949615559861, DATE('now', '-5 days')),
(15,0.35234234234234654, DATE('now', '-5 days')),
(16,0.9176647264191261, DATE('now', '-5 days')),
(17,0.939557573617809, DATE('now', '-5 days')),
(18,0.9354144394638466, DATE('now', '-5 days')),
(19,0.7475956662405586, DATE('now', '-5 days')),
(20,0.9160649941109094, DATE('now', '-5 days')),
(1,0.9031873641122599, DATE('now', '-4 days')),
(2,0.8835592744898132, DATE('now', '-4 days')),
(3,0.7896965091913037, DATE('now', '-4 days')),
(4,0.7342310240670993, DATE('now', '-4 days')),
(5,0.8658318513727998, DATE('now', '-4 days')),
(6,0.8602054673428667, DATE('now', '-4 days')),
(7,0.8486005139936013, DATE('now', '-4 days')),
(8,0.7689636850220836, DATE('now', '-4 days')),
(9,0.9952328967310304, DATE('now', '-4 days')),
(10,0.7053277363094451, DATE('now', '-4 days')),
(11,0.8266215520617575, DATE('now', '-4 days')),
(12,0.8794339566497442, DATE('now', '-4 days')),
(13,0.9340092973976643, DATE('now', '-4 days')),
(14,0.7219264190330316, DATE('now', '-4 days')),
(15,0.2134342534534534534, DATE('now', '-4 days')),
(16,0.7599132884873199, DATE('now', '-4 days')),
(17,0.7239440323512828, DATE('now', '-4 days')),
(18,0.7465700007136099, DATE('now', '-4 days')),
(19,0.759620561054238, DATE('now', '-4 days')),
(20,0.736907825584496, DATE('now', '-4 days')),
(1,0.8858043908297425, DATE('now', '-3 days')),
(2,0.9541936517107503, DATE('now', '-3 days')),
(3,0.9232013492835781, DATE('now', '-3 days')),
(4,0.8717862839638343, DATE('now', '-3 days')),
(5,0.7467599298528197, DATE('now', '-3 days')),
(6,0.7228344795577596, DATE('now', '-3 days')),
(7,0.9185288757137127, DATE('now', '-3 days')),
(8,0.9280181967158299, DATE('now', '-3 days')),
(9,0.742424778662048, DATE('now', '-3 days')),
(10,0.7507970543398621, DATE('now', '-3 days')),
(11,0.8703310864520167, DATE('now', '-3 days')),
(12,0.8319922359482709, DATE('now', '-3 days')),
(13,0.7981324984888447, DATE('now', '-3 days')),
(14,0.8928050471799686, DATE('now', '-3 days')),
(15,0.123534534675654534, DATE('now', '-3 days')),
(16,0.8078743987507638, DATE('now', '-3 days')),
(17,0.9944626974898525, DATE('now', '-3 days')),
(18,0.9914253045305268, DATE('now', '-3 days')),
(19,0.9242272695377761, DATE('now', '-3 days')),
(20,0.935449928479209, DATE('now', '-3 days')),
(1,0.7862806209920299, DATE('now', '-2 days')),
(2,0.773497098252889, DATE('now', '-2 days')),
(3,0.9861712064582289, DATE('now', '-2 days')),
(4,0.9689545020981769, DATE('now', '-2 days')),
(5,0.8468250062727614, DATE('now', '-2 days')),
(6,0.8463010404134323, DATE('now', '-2 days')),
(7,0.9673528017480569, DATE('now', '-2 days')),
(8,0.8684509359911605, DATE('now', '-2 days')),
(9,0.9782172955286601, DATE('now', '-2 days')),
(10,0.9227510462206078, DATE('now', '-2 days')),
(11,0.8786086726674408, DATE('now', '-2 days')),
(12,0.9531555392504427, DATE('now', '-2 days')),
(13,0.9575431974588158, DATE('now', '-2 days')),
(14,0.8932325362831459, DATE('now', '-2 days')),
(15,0.321543543, DATE('now', '-2 days')),
(16,0.8740555665587395, DATE('now', '-2 days')),
(17,0.8103758467725143, DATE('now', '-2 days')),
(18,0.7516342819815093, DATE('now', '-2 days')),
(19,0.7792385487502373, DATE('now', '-2 days')),
(20,0.7184573153160884, DATE('now', '-2 days')),
(1,0.8726449709157392, DATE('now', '-1 days')),
(2,0.7826707800949347, DATE('now', '-1 days')),
(3,0.7665212254432007, DATE('now', '-1 days')),
(4,0.9314409045769897, DATE('now', '-1 days')),
(5,0.8450741670997939, DATE('now', '-1 days')),
(6,0.7295358257845865, DATE('now', '-1 days')),
(7,0.9024256843429044, DATE('now', '-1 days')),
(8,0.9753533566146833, DATE('now', '-1 days')),
(9,0.8770923061288003, DATE('now', '-1 days')),
(10,0.8061294404110944, DATE('now', '-1 days')),
(11,0.852715084503899, DATE('now', '-1 days')),
(12,0.8151986616447747, DATE('now', '-1 days')),
(13,0.9977660252181659, DATE('now', '-1 days')),
(14,0.9418561997878317, DATE('now', '-1 days')),
(15,0.23424635464434, DATE('now', '-1 days')),
(16,0.7099077744614125, DATE('now', '-1 days')),
(17,0.7730727928255707, DATE('now', '-1 days')),
(18,0.8953423018889335, DATE('now', '-1 days')),
(19,0.716275947090612, DATE('now', '-1 days')),
(20,0.873241516432206, DATE('now', '-1 days')),
-- (1,0.7914010685494944, DATE('now', '-0 days')),
(2,0.8243816542500718, DATE('now', '-0 days')),
(3,0.8543707600057368, DATE('now', '-0 days')),
(4,0.9636983967061736, DATE('now', '-0 days')),
(5,0.7926651472093548, DATE('now', '-0 days')),
(6,0.8185174763256071, DATE('now', '-0 days')),
(7,0.7202317209565543, DATE('now', '-0 days')),
(8,0.886711421987148, DATE('now', '-0 days')),
(9,0.7460952579322033, DATE('now', '-0 days')),
(10,0.8538867853890517, DATE('now', '-0 days')),
(11,0.7513287811300153, DATE('now', '-0 days')),
(12,0.8084090605478946, DATE('now', '-0 days')),
(13,0.9661141231181694, DATE('now', '-0 days')),
(14,0.9481184817677852, DATE('now', '-0 days')),
(15,0.1252453452346536, DATE('now', '-0 days')),
(16,0.7145165202588856, DATE('now', '-0 days')),
(17,0.853909463837403, DATE('now', '-0 days')),
(18,0.8911659789684605, DATE('now', '-0 days')),
(19,0.8138788180287644, DATE('now', '-0 days')),
(20,0.9060129409924131, DATE('now', '-0 days'));