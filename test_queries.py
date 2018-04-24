QUERIES = {
    "health": [
        "infertility OR subfertility OR fertility OR ((tubal OR tube OR tubes OR peritubal OR oviduct) AND (block OR block* OR lesion OR disease OR factor OR occlusion OR damage OR adhesio* OR fibrosis OR obstruct*)) OR fallopian OR hydrosalpin* OR aspermi* OR oligospermia OR oligozoospermi* OR azoospermia OR asthenospermia OR asthenozoospermia OR teratospermia OR oligoasthenoteratozoospermi*",
        "(Infertility[Mesh] OR Sterility[tiab] OR Infertility[tiab] OR Subfertility[tiab] OR Sub Fertil*[tiab] OR Aspermia[tiab] OR Teratozoospermia[tiab] OR Astheno*[tiab] OR Azoospermia[tiab] OR Oligospermia[tiab] OR Hypospermatogenesis[tiab] OR Low Sperm[tiab] OR Oligozoospermia[tiab] OR Sertoli[tiab] OR Teratozoospermia[tiab] OR Abnormal Sperm*[tiab] OR Teratospermia[tiab] OR Globozoospermia[tiab] OR Polycystic Ovar*[tiab] OR Reproductive Techniques, Assisted[Mesh] OR Assisted Reproduct*[tiab] OR Assisted Conception[tiab] OR In-Vitro Fertili*[tiab] OR IFV[tiab] OR ICSI[tiab] OR IVF/ICSI[tiab] OR IUI[tiab] OR In-Vitro Matur*[tiab] OR Sperm Inject*[tiab] OR Sperm Select*[tiab] OR Intrauterine Inseminat*[tiab] OR Embryo Transfer*[tiab] OR ICSI[tiab] OR Frozen Thaw*[tiab] OR Gonadotrop*[tiab] OR Ovarian Hyperstimulat*[tiab] OR Preimplantation[tiab])",
        "(Infertility[Mesh] OR (Sterility[tiab] OR Infertility[tiab]))",
        '(A OR B[Mesh]) AND (C OR (D AND E))',
        '(((randomized controlled trial [pt]) OR (controlled clinical trial [pt]) OR (randomized [tiab]) OR (placebo [tiab]) OR (drug therapy [sh]) OR (randomly [tiab]) OR (trial [tiab]) OR (groups [tiab])  ) NOT (animals [mh] NOT humans [mh])) AND (((cardiac OR coronary OR cardiopulmonary OR myocardial OR post-cardiac OR cardio-pulmonary OR cardiovascular OR "Cardiovascular Diseases"[Mesh] OR "Arrhythmias, Cardiac"[Mesh] OR "Myocardial Infarction"[Mesh] OR "Myocardial Ischemia"[Mesh] OR "Cardiomyopathies"[Mesh]) AND (perioperative OR preoperative OR surgery OR postsurgical OR postoperative OR peri-operative OR preoperation OR preoperatively OR postoperatively OR post-operation OR operation OR post-operative OR pre-operative OR operations OR operative OR "Surgical Procedures, Operative"[Mesh] OR "General Surgery"[Mesh] OR "Perioperative Period"[Mesh] OR "Postoperative Period"[Mesh] OR "Preoperative Period"[Mesh] OR "Postoperative Complications"[Mesh])) OR ("Cardiopulmonary Bypass"[Mesh] OR "Cardiac Surgical Procedures"[Mesh] OR "Myocardial Revascularization"[Mesh] OR "Thoracic Surgery"[Mesh] OR bypass OR by-pass OR bypass-induced OR postbypass OR cabg OR ccabg OR post-cabg)) AND (statins OR statin OR pravastatin OR simvastatin OR atorvastatin OR fluvastatin OR hmg-coa OR hmg-coa-reductase)',
        'cannabi* OR marijuan* OR marihuan* OR ganja OR ganjas OR nabilo* OR CBD OR DMH-11C OR tetrahydrocannab* OR THC OR dexanabinol OR ajulemic OR dronabinol OR nabiximol* OR sativex OR endocannabi* OR levonantradol OR (faah AND (inhibitor OR hydrolase)) OR PF-04457845 OR "fatty acid amid hydrolase" OR "fatty-acid amyd hydrolase" OR "fatty acid amidohydrolase" OR cannador',
        '(Antiretroviral Therapy, Highly Active[MeSH] OR   Anti-Retroviral Agents[MeSH] OR     Antiviral Agents[MeSH:NoExp] OR     antiretrov*  OR anti-retrovir* OR "anti-retroviral" OR  HAART OR ART)',
        '(((((chronic prostatitis chronic pelvic pain syndrome[tiab] OR CP CPP*[tiab])) OR ((((("Prostatitis"[Mesh]) OR prostatit*[tiab]) OR prostatodyn*[tiab])) AND (((((((((("Asymptomatic Diseases"[Mesh]) OR asymptom*[tiab]) OR nonsymptom*[tiab]) OR non symptom*[tiab]) OR abacterial*[tiab]) OR nonbacterial*[tiab]) OR non bacterial*[tiab]) OR aseptic*[tiab]) OR nonseptic*[tiab]) OR non septic*[tiab]))) OR ((((("Prostatitis"[Mesh]) OR prostatit*[tiab]) OR prostatodyn*[tiab])) AND ((("Pelvic Pain"[Mesh]) OR pelvic pain[tiab]) OR CPP*[tiab]))))',
        '"Prostatitis"[Mesh] OR prostatit*[tiab] OR prostatodyn*[tiab] OR "Pelvic Pain"[Mesh] OR pelvic pain[tiab] OR CPP*[tiab]',
        'hemodialysis OR haemodialysis OR ((hemofiltration OR haemofiltration OR failure OR insufficiency) AND (kidney OR renal) AND chronic) OR "end-stage renal" OR "end-stage kidney" OR (endstage AND (renal OR kidney)) OR (ESRF OR ESKF OR ESRD OR ESKD) OR predialysis OR pre-dialysis OR (periton* AND dialysis) OR peritoneodialysis',
    ],
    "environment": [
        # 17
        """(Forest* OR woodland* OR “wood* pasture*” OR “wood* meadow*”)
            AND
            (Boreal OR boreonemoral OR hemiboreal OR nemoral OR temperate OR conifer* OR deciduous OR broadlea* OR “mixed forest” OR spruce OR “Scots pine” OR birch OR aspen OR beech OR “Quercus robur” OR Swed*)
            AND
            (Graz* OR brows* OR fenc* OR exclos*)
            AND
            (*Diversity OR species AND (richness OR focal OR target OR keystone OR umbrella OR red-list* OR threatened OR endangered OR rare) OR “species density” OR “number of species” OR indicator* OR abundance OR habitat*)
        """,
        # 16
        """soil* AND (arable OR agricult* OR farm* OR crop*
            OR cultivat*) AND (legume$ OR pulse$ OR “greenmanure”
            OR alfalfa$ OR lupin$ OR bean$ OR pea$
            OR lentil$ OR clover OR soy OR soybean$ OR perennial$
            OR grass* OR ley$ OR permaculture OR
            rotation OR monoculture OR “mono culture”) AND
            (“soil organic carbon” OR “soil carbon” OR “soil C”
            OR “soil organic C” OR SOC OR “carbon pool” OR
            “carbon stock” OR “carbon storage” OR “soil organic
            matter” OR SOM OR “carbon sequestrat*” OR “C
            sequestrat*”)
        """,
        # 16 google schoolar
        """soil AND carbon AND (rotation OR legume OR
            monoculture OR perennial OR fallow OR ley OR
            annual OR alfalfa OR pulse)
        """
    ]
}
