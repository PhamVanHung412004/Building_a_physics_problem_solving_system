"""
Physics Bot - A simple bot that responds to physics questions
"""

import re

# Dictionary of physics-related questions and answers
PHYSICS_RESPONSES = {
    "newton's laws": "Newton's Laws of Motion are:\n1. An object at rest stays at rest, and an object in motion stays in motion unless acted upon by an external force.\n2. Force equals mass times acceleration (F = ma).\n3. For every action, there is an equal and opposite reaction.",
    "gravity": "Gravity is the force that attracts objects with mass toward each other. On Earth, the gravitational acceleration is approximately 9.8 m/s².",
    "einstein": "Albert Einstein developed the theory of relativity, which revolutionized our understanding of space, time, and gravity. His famous equation E=mc² relates energy (E) to mass (m) multiplied by the speed of light (c) squared.",
    "quantum": "Quantum mechanics is a fundamental theory in physics that describes the physical properties of nature at the scale of atoms and subatomic particles.",
    "wave": "In physics, waves are disturbances that transfer energy without transferring matter. Examples include sound waves, light waves, and water waves.",
    "thermodynamics": "Thermodynamics is the branch of physics that deals with heat, work, and temperature, and their relation to energy, radiation, and physical properties of matter.",
    "electricity": "Electricity is the flow of electrical power or charge. It is a form of energy that comes from the movement of electrons in a conductor.",
    "magnetism": "Magnetism is a force that can attract or repel certain materials like iron. It is caused by the movement of electric charges and is closely related to electricity.",
    "optics": "Optics is the branch of physics that studies the behavior and properties of light, including its interactions with matter and the construction of instruments that use or detect it.",
    "kinetic energy": "Kinetic energy is the energy of motion. The kinetic energy of an object is related to its mass and velocity by the formula KE = (1/2)mv².",
    "potential energy": "Potential energy is stored energy that an object has due to its position or condition. Common forms include gravitational potential energy and elastic potential energy.",
    "velocity": "Velocity is a vector quantity that refers to the rate at which an object changes its position. It includes both speed and direction.",
    "acceleration": "Acceleration is the rate of change of velocity of an object with respect to time. It is a vector quantity that has both magnitude and direction.",
    "momentum": "Momentum is a vector quantity equal to the product of an object's mass and velocity. The formula is p = mv.",
    "energy conservation": "The principle of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another.",
    "relativity": "Einstein's theory of relativity consists of two parts: the Special Theory of Relativity (1905) which deals with the constancy of the speed of light and the equivalence of mass and energy, and the General Theory of Relativity (1915) which deals with gravity as a geometric property of space and time.",
    "quantum mechanics": "Quantum mechanics is a fundamental theory in physics that provides a description of the physical properties of nature at the scale of atoms and subatomic particles. It departs from classical mechanics primarily at the quantum realm of atomic and subatomic length scales.",
    "particle physics": "Particle physics is the branch of physics that studies the nature of the particles that constitute matter and radiation.",
    "string theory": "String theory is a theoretical framework in which the point-like particles of particle physics are replaced by one-dimensional objects called strings. It attempts to reconcile quantum mechanics and general relativity.",
    "electromagnetism": "Electromagnetism is a branch of physics involving the study of the electromagnetic force, a type of physical interaction that occurs between electrically charged particles.",
    "nuclear physics": "Nuclear physics is the field of physics that studies atomic nuclei and their constituents and interactions.",
    "fluid dynamics": "Fluid dynamics is the branch of physics and engineering that studies the flow of fluids (liquids and gases).",
    "sound": "Sound is a vibration that propagates as an acoustic wave, through a transmission medium such as a gas, liquid or solid.",
    "light": "Light is electromagnetic radiation within the portion of the electromagnetic spectrum that can be perceived by the human eye.",
    "heat": "Heat is the transfer of energy from one system to another as a result of thermal interactions.",
    "pressure": "Pressure is the force applied perpendicular to the surface of an object per unit area over which that force is distributed.",
    "friction": "Friction is the force resisting the relative motion of solid surfaces, fluid layers, and material elements sliding against each other.",
    "work": "In physics, work is the energy transferred to or from an object via the application of force along a displacement.",
    "power": "Power is the rate at which work is done or energy is transferred. It is measured in watts (W).",
    "ohm's law": "Ohm's law states that the current through a conductor between two points is directly proportional to the voltage across the two points. The formula is I = V/R, where I is current, V is voltage, and R is resistance.",
    "circuit": "An electric circuit is a path in which electrons from a voltage or current source flow. The point where those electrons enter an electrical circuit is called the 'source' of electrons.",
    "atom": "An atom is the smallest unit of ordinary matter that forms a chemical element. Every solid, liquid, gas, and plasma is composed of neutral or ionized atoms.",
    "nucleus": "The nucleus is the small, dense region consisting of protons and neutrons at the center of an atom.",
    "electron": "The electron is a subatomic particle with a negative elementary electric charge. It orbits around the nucleus of an atom.",
    "proton": "A proton is a subatomic particle with a positive electric charge. Protons, along with neutrons, make up the nucleus of an atom.",
    "neutron": "A neutron is a subatomic particle with no electric charge. Neutrons, along with protons, make up the nucleus of an atom.",
    "photon": "A photon is a particle of light. It is the quantum of the electromagnetic field including electromagnetic radiation, and the force carrier for the electromagnetic force.",
    "speed of light": "The speed of light in a vacuum is a universal physical constant that is exactly equal to 299,792,458 meters per second (approximately 186,282 miles per second).",
    "e=mc2": "E=mc² is Einstein's famous equation that expresses the equivalence of mass and energy. It states that the energy (E) equals the mass (m) multiplied by the speed of light (c) squared.",
    "radioactivity": "Radioactivity is the spontaneous emission of radiation from the nucleus of an unstable atom due to a variety of processes.",
    "half-life": "Half-life is the time required for a quantity to reduce to half of its initial value. The term is commonly used in nuclear physics to describe how quickly unstable atoms undergo radioactive decay.",
    "fusion": "Nuclear fusion is a reaction in which two or more atomic nuclei are combined to form one or more different atomic nuclei and subatomic particles. It's the process that powers the Sun and other stars.",
    "fission": "Nuclear fission is a reaction in which the nucleus of an atom splits into two or more smaller nuclei. It's the process used in nuclear power plants and atomic bombs.",
    "black hole": "A black hole is a region of spacetime where gravity is so strong that nothing, including light, can escape from it.",
    "universe": "The universe is all of space and time and their contents, including planets, stars, galaxies, and all other forms of matter and energy.",
    "big bang": "The Big Bang theory is the prevailing cosmological model explaining the existence of the observable universe from the earliest known periods through its subsequent large-scale evolution.",
    "dark matter": "Dark matter is a hypothetical form of matter that is thought to account for approximately 85% of the matter in the universe. It doesn't interact with the electromagnetic force but would still have gravitational effects on ordinary matter.",
    "dark energy": "Dark energy is a hypothetical form of energy that permeates all of space and tends to accelerate the expansion of the universe.",
    "higgs boson": "The Higgs boson is an elementary particle in the Standard Model of particle physics, produced by the quantum excitation of the Higgs field. It explains why some fundamental particles have mass.",
    "standard model": "The Standard Model of particle physics is the theory describing three of the four known fundamental forces in the universe (electromagnetic, weak, and strong), as well as classifying all known elementary particles."
}

def get_physics_response(question):
    """
    Generate a response to a physics-related question.
    
    Args:
        question (str): The user's physics question
        
    Returns:
        str: The physics bot's response
    """
    # Convert question to lowercase for case-insensitive matching
    question_lower = question.lower()
    
    # Check if this is a greeting
    greeting_pattern = r'\b(hi|hello|hey|greetings|howdy)\b'
    if re.search(greeting_pattern, question_lower):
        return "Hello! I'm Physics Bot. Ask me any physics-related question, and I'll do my best to answer."
    
    # Check if this is a thank you
    thanks_pattern = r'\b(thanks|thank you|thank you very much|appreciate it)\b'
    if re.search(thanks_pattern, question_lower):
        return "You're welcome! Feel free to ask more physics questions."
    
    # Check for best match in our knowledge base
    best_match = None
    best_score = 0
    
    for key in PHYSICS_RESPONSES:
        if key in question_lower:
            # Direct match
            return PHYSICS_RESPONSES[key]
        
        # Check for partial matches
        score = sum(1 for word in key.split() if word in question_lower.split())
        if score > best_score:
            best_score = score
            best_match = key
    
    # If we found a good partial match
    if best_score > 0:
        return PHYSICS_RESPONSES[best_match]
    
    # Default response
    return "I'm not sure about that specific physics concept. Try asking about Newton's laws, gravity, relativity, quantum mechanics, or other fundamental physics topics."
